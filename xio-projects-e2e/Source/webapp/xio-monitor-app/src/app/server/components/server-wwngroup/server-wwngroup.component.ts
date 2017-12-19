import {Component, OnDestroy, OnInit} from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { State} from '../../../reducers/index';
import { Store } from '@ngrx/store';
import { ServermanagementService } from '../../service/servermanagement.service';
import { getServerSideWwnGroups } from '../../../reducers/index';
import { UpdateServerAction, GetServerSideWwnGroupAction } from '../../../actions/server.actions';
import { SnackbarService, XioProgressComponent } from '../../../theme/';
import { MdDialog } from '@angular/material';


@Component({
  selector: 'app-server-wwngroup',
  templateUrl: './server-wwngroup.component.html',
  styleUrls: ['./server-wwngroup.component.scss']
})
export class ServerWwngroupComponent implements OnInit, OnDestroy {

	public ser_id: any;
  public sangroup_id: any;
  public server_name: any;
  public ise_list: any[];
  public ise_id;
  public wwnGroups$;
  public ise_wnn_list: any[];
  public ise_wnn_all_list: any[];
  public loading_stack: any;
  public server_added_list: any[];
  public server_removed_list: any[];


   constructor( public router: Router,
                public route: ActivatedRoute,
                public dialog: MdDialog,
                public snackbarService: SnackbarService,
                public servermgmt: ServermanagementService,
                public store: Store<State>) {

    this.ise_wnn_list = [];
    this.ise_wnn_all_list = [];
    this.loading_stack = {
      wwngroup_details: false,
      wwngroup_details_text: 'Loading List of WWN groups.....'
    };
    this.server_added_list = [];
    this.server_removed_list = [];

  }

  ngOnInit() {
    this.loading_stack.wwngroup_details = false;
    this.route.params.subscribe(params => {
      this.ser_id = params['ser_id'];
      this.sangroup_id = params['sangroup_id'];
      this.loading_stack.wwngroup_details = false;
      this.ise_wnn_list = [];
      this.allWwnGroups();
    });
  }

  /**
   *  This method is used for navigating to WWN Edit
   * @param event
   * @param {string} ser_id
   */
  navigateTo(event: any, ser_id: string) {
    this.router.navigate(['/' + this.ser_id + '/wwn/']);
  }

  /**
   * This method used for checking is Object empty or not
   * @param obj
   * @returns {boolean}
   */
  isEmpty(obj) {
    return Object.keys(obj).length === 0;
  }

  /**
   *
   */
  allWwnGroups() {
    this.loading_stack.wwngroup_details = false;
    let payLoad = {
                    'server_id': this.ser_id,
                    'sangroup_id': this.sangroup_id
                  };
    this.store.dispatch(new GetServerSideWwnGroupAction(payLoad));
    this.wwnGroups$ = this.store.select(getServerSideWwnGroups).subscribe(res => {
        if (!this.isEmpty(res)) {
          this.loading_stack.wwngroup_details = true;
          this.server_name = res['server'] !== undefined ? res['server']['server_name'] : '';
          this.ise_wnn_list = res['ises'] !== undefined ? res['ises'] : [];
        }
    });

  }

  /**
   * This method is used for mapping and unmapping wwn group to server
   * @param e
   * @param wwn
   * @param ise_id
   */
   togglewwn(e, wwn, ise_id) {

    if (e.checked) {
      for (let i = 0; i < this.server_removed_list.length; i++) {
        if (wwn === this.server_removed_list[i]['wwngroup']) {
          this.server_removed_list.splice(i, 1);
        }
      }
      this.server_added_list.push({
        'wwngroup': wwn,
        'ise_id': ise_id
      });
    } else {
      for (let i = 0; i < this.server_added_list.length; i++) {
        if (wwn === this.server_added_list[i]['wwngroup']) {
          this.server_added_list.splice(i, 1);
        }
      }

      this.server_removed_list.push({
        'wwngroup': wwn,
        'ise_id': ise_id
      });
    }
  }


  /**
   * This method calls for back end service for updating wwn group to server
   */
  onUpdate() {
   let payLoad = {
      'server_id': this.ser_id,
      'sangroup_id': this.sangroup_id
    };
    const progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
    progressRef.componentInstance.progress_data = 'Loading....';
    this.store.dispatch(new UpdateServerAction({
      added: this.server_added_list,
      removed: this.server_removed_list,
      server_id: this.ser_id,
      server_name: this.server_name,
      cb: (res, err) => {
        if (res) {
          progressRef.close();
          this.ise_wnn_list.length = 0;
          this.loading_stack.wwngroup_details = false;
          this.store.dispatch(new GetServerSideWwnGroupAction(payLoad));
          this.snackbarService.toastMe('Server WwnGroup Updated Successfully', 2000);
        } else if (err) {
          progressRef.close();
          console.error(err);
        }
      }
    }));
  }

  ngOnDestroy() {
    this.loading_stack.wwngroup_details = false;
    this.ise_wnn_list.length = 0;
  }

}







