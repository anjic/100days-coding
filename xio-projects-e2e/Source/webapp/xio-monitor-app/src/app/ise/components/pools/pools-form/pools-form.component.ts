import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormBuilder, FormGroup, FormArray, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { PoolsService } from './../../../services/pools.service';
import { MdDialog } from '@angular/material';
import { SnackbarService, XioProgressComponent, XioAlertComponent } from './../../../../theme/';
import { PoolsUtil } from '../../../../common/utils/PoolsUtil';
import { Pools } from '../../../models/pools';
import {Store} from '@ngrx/store';
import {State,  getMediumListState} from '../../../../reducers/';
import {GetMediumAction, ExpandPoolAction, CreatePoolAction} from '../../../../actions/pools.actions';


@Component({
  selector: 'app-pools-form',
  templateUrl: './pools-form.component.html',
  styleUrls: ['./pools-form.component.scss']
})
export class PoolsFormComponent extends PoolsUtil  implements OnInit, OnDestroy {

  public ise_id;
  public pool_id;
  public poolform: FormGroup;
  public loading_stack;
  public medium_obs$;
  public medium_list: Array<Object>;
  public progressRef;
  public poolName;


  onCallBack = this.onCallBack || ((sucess, error) => {
    if ( !error ) {
      this.snackbarService.toastMe('Pool ' + (this.pool_id ? 'Updated' : 'Created' ) + ' Successfully', 2000);
      this.router.navigate(['ise/' + this.ise_id + '/pools/']);
    } else {
      this.catchError( error );
   }
    this.progressRef.close();
    this.progressRef = null;
});


  /**
   * @param {FormBuilder} formBuilder
   * @param {ActivatedRoute} activatedRoute
   * @param {Router} router
   * @param {PoolsService} poolService
   * @param {MdDialog} dialog
   * @param {SnackbarService} snackbarService
   * @param {Store<State>} store
   */

  constructor(public formBuilder: FormBuilder,
              public activatedRoute: ActivatedRoute,
              public router: Router,
              public poolService: PoolsService,
              public dialog: MdDialog,
              public snackbarService: SnackbarService,
              public store:Store<State>) {
    super();
    this.loading_stack = {
      media_list: false,
      media_list_text: 'Loading.....'
    };
  }

  ngOnInit() {
    this.poolform = this.formBuilder.group({
      id: [''],
      media: this.formBuilder.array([]),
      assigned_media: this.formBuilder.array([])
    });

    this.activatedRoute.params.subscribe(
      params => {
        if ( params && params['pool_id']) {
          this.pool_id = params['pool_id'];
        }
        if (params && params['pool_name']) {
          this.poolName = params['pool_name'].replace('_', ' ' );
        }

      });

    this.medium_obs$ = this.store.select(getMediumListState).subscribe((data: Array<Pools>) =>{
      if ( !this.isEmpty(data) ) {

          this.medium_list= data;
          this.addMediumControl(data);
          this.loading_stack.media_list = false;

       }
    }, error => {
      this.catchError( error );

    });

    this.activatedRoute.parent.params.subscribe(
      params => {
        this.ise_id = params['ise_id'];
        this.loading_stack.media_list = true;
        this.store.dispatch(new GetMediumAction(this.ise_id));
      });
  }

  /**
   * Add Medium Control
   * @namespace xio.PoolsFormComponent
   * @method addMediumControl
   * @return {void}
   */
  addMediumControl(data) {
    if ( data !== undefined ) {
      for (let media of this.medium_list) {
        let type_media: String = media['status']['details']['detail'] === 'Offline: Ready to add' 
                                                                        ? 'media' : 'assigned_media',
          status = this.pool_id && this.pool_id === media['pool']['globalid'];

        if (type_media) {
          let dp_obj = {
            media_id: media['id'],
            dp_label: 'Open Datapac ' + media['id'],
            status: status,
            type_media: type_media,
            dp_status: media['status']['_attr']['string'],
            dp_redundancyhealth: media['redundancyhealth']['healthstring']
          };
          this.addMedia(dp_obj);
        }
      }
    }
  }

  /**
   * submit controller
   * @namespace xio.PoolsFormComponent
   * @method onSubmit
   * @return {void}
   */
  onSubmit() {
    let media = [];
    for (let control of this.poolform['controls']['media'].value) {
      if (control.dp) {
        media.push(control.id);
      }
    }

     let data = {
        media: media.join(',')
      },

      fnToCall = this.pool_id ? 'expandPool' : 'createPool';
      this.progressRef = this.dialog.open(XioProgressComponent, {disableClose: true});
      this.progressRef.componentInstance.progress_data = 'processing';
      let payLoad = {
        'media' : data,
        'ise_id' : this.ise_id,
        'pool_id' : this.pool_id,
        'cb': this.onCallBack
      };
      this.store.dispatch(this.pool_id ? new ExpandPoolAction(payLoad) : new CreatePoolAction(payLoad));


  }


  /**
   * navigating to particular path
   * @namespace xio.PoolsFormComponent
   * @method navigateTo
   */

  navigateTo(event: any) {
    event.stopPropagation();
    let path: String = '/ise/' + this.ise_id + '/pools';
    this.router.navigate([path]);
  }

  /**
   * catching Error and displaying in Popup
   * @namespace xio.PoolsFormComponent
   * @param {any} _error
   * @method catchError
   */

  catchError (_error) {
    let err_msg = (_error.json !== '' || _error.json !== undefined
      || _error.json !== null) ? _error.json() : '';
    let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
    alertRef.componentInstance.title = 'Pools';
    alertRef.componentInstance.message = err_msg !== '' ?
      err_msg.result.error.message :
      'Bad Request';
  }


  ngOnDestroy() {
    if ( this.medium_obs$ ) {
      this.medium_obs$.unsubscribe();  
    }
     window.removeEventListener('click', this.onSubmit.bind(this), false);    
     window.removeEventListener('click', this.navigateTo.bind(this), false);    
  }
}
