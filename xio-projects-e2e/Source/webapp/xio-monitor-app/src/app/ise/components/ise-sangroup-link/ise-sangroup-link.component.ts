import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, FormArray, Validators} from '@angular/forms';
import {Router, ActivatedRoute} from '@angular/router';
import {IseService} from './../../services/ise.service';
import {SangroupService} from '../../../san-group/services/sangroup.service';
import {MdDialog} from '@angular/material';
import {MenuContentService, SnackbarService, XioProgressComponent} from './../../../theme/index';
import {SanGroupUtil} from '../../../common/utils/SanGroupUtil';
import {State} from '../../../reducers/index';
import {Store} from '@ngrx/store';
import {ChangeISELink, GetISESanGroup, SetISEId} from '../../../actions/ise-management.actions';
import {GetMenuAction} from '../../../actions/menu.action';

@Component({
  selector: 'app-ise-sangroup-link',
  templateUrl: './ise-sangroup-link.component.html',
  styleUrls: ['./ise-sangroup-link.component.scss'],
})
export class IseSangroupLinkComponent extends SanGroupUtil implements OnInit {


  public ise_id: number;
  public linkForm: FormGroup;

  constructor(public fb: FormBuilder,
              public ises: IseService,
              public sgs: SangroupService,
              public route: ActivatedRoute,
              public router: Router,
              public snackbarService: SnackbarService,
              public dialog: MdDialog,
              public mcs: MenuContentService,
              public store: Store<State>) {
    super();
  }

  ngOnInit() {
    this.linkForm = this.fb.group({
      ise_id: [''],
      ise_name: [''],
      available_sg: this.fb.array([]),
      current_sg: this.fb.array([])
    });

    this.route.params.subscribe(params => {
      this.ise_id = params['ise_id'];
      this.linkForm['controls']['ise_id'].setValue(this.ise_id);
      this.store.dispatch(new SetISEId(this.ise_id));
      this.store.dispatch(new GetISESanGroup({
        ise_id: this.ise_id,
        cb: (res) => {
          if ( res) {
            for (let i in res) {
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
  initSG(v: number, lbl: string, status: boolean) {
    return this.fb.group({sg: [status, Validators.required], label: lbl, sangroup_id: v});
  }

  /**
   * add SG
   * @namespace xio.IseSangroupLinkComponent
   * @method addSG
   * @return {void}
   */
  addSG(v: number, lbl: string, type: string, status: boolean) {
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
  UpdateISESangroupLink() {
    let progressRef = this.dialog.open(XioProgressComponent, {disableClose: true});
    let progress_data = 'processing';
    progressRef.componentInstance.progress_data = progress_data;
    this.store.dispatch(new ChangeISELink({
      ise_sangroup_data: this.linkForm.value,
      cb: () => {
        progressRef.close();
        // TODO Dominic: Why getAll SAN's here ??? -- Have to update Menu Content
        // Discuss with madu to change the service response / update the store manually
        this.sgs.getAll().subscribe(
          sgsRes => {
            this.snackbarService.toastMe('Ise-Sangroup Updated Successfully', 2000);
            // this.store.dispatch(new GetAllAction({}));
            this.store.dispatch(new GetMenuAction({}));
          }
        );
        this.router.navigate(['/ise/']);
      }
    }));
    // this.ises.updateISESangroupLink(this.linkForm.value).subscribe(
    //   res => {
    //     progressRef.close();
    //     // TODO Dominic: Why getAll SAN's here ??? -- Have to update Menu Content
    //     // Discuss with madu to change the service response / update the store manually
    //     this.sgs.getAll().subscribe(
    //       sgsRes => {
    //         this.snackbarService.toastMe('Ise-Sangroup Updated Successfully', 1000);
    //         this.mcs.get().subscribe();
    //       }
    //     );
    //     this.router.navigate(['/ise/']);
    //   }
    // );
  }


}
