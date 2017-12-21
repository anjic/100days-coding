import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { IseService } from '../../../ise/services/ise.service';
import { getISEId, State, getAllIseLst, getISEInfo } from '../../../reducers/index';
import { Store } from '@ngrx/store';
import { GetAllISEList } from '../../../actions/ise-management.actions';
import { ServermanagementService } from '../../service/servermanagement.service';
import { getServerWwnGroups } from '../../../reducers/index';
import { GetAllWwnGroupAction, UpdateServerAction } from '../../../actions/server.actions';
import { SnackbarService, MenuContentService, XioProgressComponent, XioDialogComponent, XioAlertComponent } from '../../../theme/';
import { MdDialog } from '@angular/material';
import {GetMenuAction} from "../../../actions/menu.action";



@Component({
  selector: 'app-server-edit-form',
  templateUrl: './server-edit-form.component.html',
  styleUrls: ['./server-edit-form.component.scss']
})
export class ServerEditFormComponent implements OnInit {
  public ser_id: any;
  public server_name: any;
  public ise_list: any[];
  public ise_id;
  public wwnGroups$;
  public ise_wnn_list: any[];
  public ise_wnn_all_list: any[];
  public loading_stack: any;
  public server_added_list: any[];
  public server_removed_list: any[];

  constructor(public router: Router,
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
    this.route.params.subscribe(params => {
      this.loading_stack.wwngroup_details = false;
      this.ser_id = params['ser_id'];
      this.ise_wnn_list.length = 0;
      this.allWwnGroups();
    });
  }


  navigateTo(event: any, ser_id: string) {
    this.router.navigate(['/' + this.ser_id + '/wwn/']);
  }

  isEmpty(obj) {
    return Object.keys(obj).length === 0;
  }


  allWwnGroups() {
    this.loading_stack.wwngroup_details = false;
    this.store.dispatch(new GetAllWwnGroupAction(this.ser_id));
    this.wwnGroups$ = this.store.select(getServerWwnGroups).subscribe(
      data => {
        if (!this.isEmpty(data)) {
          this.loading_stack.wwngroup_details = true;
          this.server_name = data['server'] !== undefined ? data['server']['server_name'] : '';
          this.ise_wnn_list = data['ises'] !== undefined ? data['ises'] : [];
        }
      });
  }

  /**
   * This method used adding WWN's
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

  onUpdate() {
    let PayLoad = {
      'server_id': this.ser_id
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
          this.server_removed_list.length = 0;
          this.server_added_list.length = 0;
          progressRef.close();
          this.ise_wnn_list.length = 0;
          this.loading_stack.wwngroup_details = false;
          this.store.dispatch(new GetAllWwnGroupAction(this.ser_id));
          this.store.dispatch(new GetMenuAction({}));
          this.snackbarService.toastMe('Server WwnGroup Updated Successfully', 2000);
        }else if (err) {
          progressRef.close();
        }
      }
    }));
  }

}






