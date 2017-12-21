import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { MdDialog } from '@angular/material';
import { Store } from '@ngrx/store';
import { AddServerAction, GetServerAction, UpdateServerAction } from '../../../actions/server.actions';
import { GetMenuAction } from "../../../actions/menu.action";
import { SnackbarService, XioProgressComponent, MenuContentService, XioAlertComponent } from './../../../theme/';
import { getServerState, getSanGroupLst, State } from '../../../reducers';
import { SanGroupUtil } from '../../../common/utils/SanGroupUtil';
import { GetAllAction } from '../../../actions/sangroup.action';
import { ServermanagementService } from '../../service/servermanagement.service';


@Component({
  selector: 'app-server-form',
  templateUrl: './server-form.component.html',
  styleUrls: ['./server-form.component.scss']
})
export class ServerFormComponent extends SanGroupUtil implements OnInit {

  public serverForm: FormGroup;
  public ser_id;
  public server_list: any[];
  public sangroup_list: any[];
  public sanGroup$;
  public sangroup_loaded

  constructor(public fb: FormBuilder,
    public router: Router,
    public route: ActivatedRoute,
    public snackbarService: SnackbarService,
    public servermgmt: ServermanagementService,
    public dialog: MdDialog,
    public mcs: MenuContentService,
    public store: Store<State>

  ) {
    super();
    this.sangroup_loaded = {
      sg: false,
      sg_text: "Loading...."

    }
  }

  ngOnInit() {

    this.serverForm = this.fb.group({
      server_name: ['', [Validators.required,
      Validators.pattern(/^[a-zA-Z0-9\-_.,!@#$%^*();:,\s]+$/)]],
      sangroup: this.fb.array([]),
      comment: [''],
      created_by: '1',
      modified_by: '1',
    });

    this.route.params.subscribe(params => {
      this.ser_id = params['ser_id'];

    });
        this.sangroup_loaded.sg = true;
    this.sanGroup$ = this.store.select(getSanGroupLst).subscribe(
      data => {
        if (!this.isEmpty(data) && data instanceof Array)
        this.sangroup_loaded.sg = false;
        this.serverForm['controls']['sangroup'] = this.fb.array([]);
        for (let i = 0; i < data.length; i++) {
          let v = data[i]['sangroup_id'];
          let lbl = data[i]['sangroup_name'];
          this.addServerSG(v, lbl, 'sangroup', false);
        }
        this.sangroup_list = data;
      });

  }

  navigateTo(event: any, path: string) {
    event.stopPropagation();
    this.router.navigate([path]);
  }

  sanCheckBoxChange(e) {
    this.sangroup_list.forEach((s) => {
      if (s.sangroup_id == e.source.value) {
        s['selected'] = e.checked;
      }
    });
  }

  isEmpty(obj) {
    return Object.keys(obj).length === 0;
  }

  onSaveCallBack = this.onSaveCallBack || ((success, error) => {
    let progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
    progressRef.componentInstance.progress_data = 'Processing....';
    if (!error) {
      this.sangroup_list.forEach((s) => {
          s['selected'] = false;
      });
      progressRef.close();
      this.snackbarService.toastMe('Server created Successfully', 2000);
      this.store.dispatch(new GetMenuAction({}));
      this.router.navigate(['/server/list/']);
    } else {

      progressRef.close();
      console.log(error);
      this.serverForm['controls']['server_name'].setErrors({
        remote: true
      });

    }
  });

  onSubmit() {
    let data = this.serverForm.value;
    delete data['sangroup'];
    data['sangroup'] = [];
    for (let i = 0; i < this.sangroup_list.length; i++) {
      if (this.sangroup_list[i].hasOwnProperty('selected') &&
        this.sangroup_list[i]['selected']) {
        data['sangroup'].push(this.sangroup_list[i]['sangroup_id'])
      }
    }
    data.cb = this.onSaveCallBack;
    this.store.dispatch(new AddServerAction(data));

  }


}


