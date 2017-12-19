import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup, FormArray, Validators} from '@angular/forms';
import {Router, ActivatedRoute} from '@angular/router';
import {SangroupService} from '../../../san-group/services/sangroup.service';
import {MdDialog} from '@angular/material';
import {MenuContentService, SnackbarService, XioProgressComponent} from './../../../theme/index';
import {SanGroupUtil} from '../../../common/utils/SanGroupUtil';
import {State} from "../../../reducers/index";
import {Store} from '@ngrx/store';
import {ChangeServerLink, GetServerSanGroup} from "../../../actions/server.actions";
import {GetAllAction} from "../../../actions/sangroup.action";
import {GetMenuAction} from "../../../actions/menu.action";
@Component({
  selector: 'app-server-sangroup-link',
  templateUrl: './server-sangroup-link.component.html',
  styleUrls: ['./server-sangroup-link.component.scss']
})
export class ServerSangroupLinkComponent implements OnInit {


  public server_id: number;
  public ise_id: number;
  public linkForm: FormGroup;

  constructor(public fb: FormBuilder,
              public sgs: SangroupService,
              public route: ActivatedRoute,
              public router: Router,
              public snackbarService: SnackbarService,
              public dialog: MdDialog,
              public mcs: MenuContentService,
              public store: Store<State>) {
    // super();
  }

  ngOnInit() {
    this.linkForm = this.fb.group({
      ser_id: [''],
      ise_name: [''],
      available_sg: this.fb.array([]),
      current_sg: this.fb.array([])
    });

    this.route.params.subscribe(params => {
      this.server_id = params['ser_id'];
      this.linkForm['controls']['ser_id'].setValue(this.server_id);
      this.store.dispatch(new GetServerSanGroup({
        server_id: this.server_id,
        cb: (res) => {
          if (res) {
            for(let i in res) {
              let chk = res[i]['checked'];
              this.addSG(res[i]['sangroup_id'],
                res[i]['sangroup_name'],
                (chk ? 'current_sg' : 'available_sg'), chk);
            }
          }
        }
      }));
    });


  }

  /**
   * init SG
   * @namespace xio.IseSangroupLinkComponent
   * @method initSG
   * @return {FormGroup}
   */
  initSG(v: string, lbl: string, status: boolean) {
    return this.fb.group({sg: [status, Validators.required], label: lbl, sangroup_id: v});
  }

  /**
   * add SG
   * @namespace xio.IseSangroupLinkComponent
   * @method addSG
   * @return {void}
   */
  addSG(v: string, lbl: string, type: string, status: boolean) {
    const control = <FormArray> this.linkForm['controls'][type];
    control.push(this.initSG(v, lbl, status));
  }

  /**
   * get SG Lbl
   * @namespace xio.IseSangroupLinkComponent
   * @method getSGLabel
   * @return {string}
   */
  getSGLabel(type: string, i: number) {
    const control = <FormArray> this.linkForm['controls'][type];
    return control.value[i].label;
  }

  /**
   * update ISE Sangroup Link
   * @namespace xio.IseSangroupLinkComponent
   * @method UpdateISESangroupLink
   * @return {void}
   */
  UpdateServerSangroupLink() {
    let progressRef = this.dialog.open(XioProgressComponent, {disableClose: true});
    let progress_data = 'processing';
    progressRef.componentInstance.progress_data = progress_data;
    this.store.dispatch(new ChangeServerLink({
      server_sangroup_data: this.linkForm.value,
      server_id : this.server_id,
      cb: (success, error) => {
        if (!error) {
          progressRef.close();
          this.snackbarService.toastMe('Server-Sangroup Updated Successfully', 2000);
          this.store.dispatch(new GetMenuAction({}));
          this.router.navigate(['/server/']);
        }else {
          progressRef.close();
          console.log(error);
        }
      }
    }));
  }


}
