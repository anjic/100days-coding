
/**
 * Created by Venkatesh
 */

import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { MdDialog } from '@angular/material';
import { XioDialogComponent, XioProgressComponent, XioAlertComponent, SnackbarService } from './../../../../theme/';
import { poolsListOptions } from './pools-list-options';
import { CommonUtil } from '../../../../common/utils/CommonUtil';
import { Pools } from '../../../models/pools';
import { Drives } from '../../../models/drives';
import { Store } from '@ngrx/store';
import { State, getAllPoolsState, getDrivesListState } from '../../../../reducers/';
import { SetISEId } from '../../../../actions/ise-management.actions';
import {
  GetAllPoolsAction, DeletePoolAction, Reset,
  UpdateDrivesIdentifyAction, GetDrivesAction
} from '../../../../actions/pools.actions';



@Component({
  selector: 'app-pools-list',
  templateUrl: './pools-list.component.html',
  styleUrls: ['./pools-list.component.scss']
})
export class PoolsListComponent extends CommonUtil implements OnInit, OnDestroy {

  public gridOptions;
  public poolGridOptions = {};
  public ise_id;
  public pools_datapac_list: any = [];
  public pools_datapac_label: any = [];

  // Pools List
  public pools_list: Array<Pools>;
  // Drives List
  public datapac_list: any = [];

  public drive_track_list: any = { left: [], right: [] };
  public loading_stack;
  public all_pools_state_obs$;
  public progressRef;

    /**
   *
   * @type {any|((success, error)=>any)}
   */
  onPoolDeleteCallBack = this.onPoolDeleteCallBack || ((success, error) => {
    if (!error) {
      this.getPoolsList(this.ise_id);
      this.snackBarService.toastMe('Pool Deleted Successfully', 2000);
    } else {
      let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
          alertRef.componentInstance.title = 'Pool Delete';
          alertRef.componentInstance.message = error.json().result.error.message;
    }
    this.progressRef.close();
    this.progressRef = null;
  });

  /**
   *
   * @param {ActivatedRoute} activatedRoute
   * @param {Router} router
   * @param {MdDialog} dialog
   * @param {SnackbarService} snackbarService
   * @param {Store<State>} store
   */
  constructor(public activatedRoute: ActivatedRoute,
              public router: Router,
              public dialog: MdDialog,
              public snackBarService: SnackbarService,
              public store: Store<State>) {
        super();
        this.pools_list = [];
        this.loading_stack = {
          drive_list: false,
          drive_list_text: 'Loading drives.....',
          pool_list: false,
          pool_list_text: 'Loading pools.....'
        };
  }


  ngOnInit() {
    this.gridOptions = poolsListOptions;
    this.activatedRoute.parent.params.subscribe(
      params => {
        this.ise_id = params['ise_id'];
        this.store.dispatch(new SetISEId(this.ise_id));
        this.getDriveList();
    });
    this.loading_stack.drive_list = true;
    this.loading_stack.pool_list = true;
  }


 /**
  * controller to getMenuContent Drive List
  * @namespace xio.PoolsListComponent
  * @method getDriveList
  * @return {void}
 */

  getDriveList() {
    this.store.dispatch(new GetDrivesAction({
      ise_id: this.ise_id,
      cb: (success, error) => {
        if (!error) {
          this.store.select( getDrivesListState ).subscribe(( data: Array<Drives> ) => {
            if ( data ) {
              this.pools_datapac_label = [];
              this.drive_track_list = { left: [], right: [] };
              this.datapac_list = [];

              this.pools_datapac_label = {
                left: [{
                  label: 'Open DataPac 1',
                  pool_label: ''
                }, {
                  label: 'Open DataPac 3',
                  pool_label: ''
                }, {
                  label: 'Open DataPac 5',
                  pool_label: ''
                }],
                right: [{
                  label: 'Open DataPac 6',
                  pool_label: ''
                }, {
                  label: 'Open DataPac 4',
                  pool_label: ''
                }, {
                  label: 'Open DataPac 2',
                  pool_label: ''
                }]
              };

              this.loading_stack.drive_list = false;

              // for (let i = 0; this.ps.drives_list.length > 0; i++) {
              //   if (!(i % 2)) {
              //     this.drive_track_list.left.push(this.ps.drives_list.splice(0, 10));
              //   }
              //   else {
              //     this.drive_track_list.right.push(this.ps.drives_list.splice(0, 10));
              //   }

              // }
              // Left Side Drive
              this.drive_track_list.left.push(data.slice(0, 5));
              this.drive_track_list.left.push(data.slice(5, 10));
              this.drive_track_list.left.push(data.slice(20, 25));
              this.drive_track_list.left.push(data.slice(25, 30));
              this.drive_track_list.left.push(data.slice(40, 45));
              this.drive_track_list.left.push(data.slice(45, 50));

              // Right Side Drive
              this.drive_track_list.right.push(data.slice(55, 60));
              this.drive_track_list.right.push(data.slice(50, 55));
              this.drive_track_list.right.push(data.slice(35, 40));
              this.drive_track_list.right.push(data.slice(30, 35));
              this.drive_track_list.right.push(data.slice(15, 20));
              this.drive_track_list.right.push(data.slice(10, 15));

              console.log('drive_track_list..:', this.drive_track_list);

              let poolsDataArr = {
                left: [0, 20, 40],
                right: [50, 30, 10]
              };
            
              // to describe in which pool the Datapac is assigned
              for ( let poolData in poolsDataArr ) {
                let cnt = 0;
                if ( poolData ) {
                  for ( let pools of poolsDataArr[poolData] ) {
                    this.pools_datapac_label[poolData][cnt]['pool_label'] =
                      (data[pools] && data[pools]['pool'] && data[pools]['pool']['poolid'])
                        ? 'Pool ' + data[pools]['pool']['poolid']
                        : 'Unassigned';
                    cnt++;
                  }
                }                
              }

             // constructing a datapac _list 
              for (let dataPac of data) {
                let _medium = dataPac['medium']._attr.self.split('/').pop();
                if (!this.datapac_list[_medium]) {
                  this.datapac_list[_medium] = {
                    id: _medium,
                    drive: [],
                    gridOptions: this.gridOptions,
                    show: true
                  };
                }
                this.datapac_list[_medium].drive.push(dataPac);
              }
              this.getPoolsList(this.ise_id);
            }
          }, _error => {
            this.catchError(_error);            
          });
        } else {
          this.catchError(error);   
      }
    }

    }));
  }

  /**
   * call resize util method to span column width across container
   * **/
  expandPool(gridOptions) {
    if (this.poolGridOptions.hasOwnProperty(gridOptions.getAttribute('globalid'))) {
        this.poolGridOptions[gridOptions.getAttribute('globalid')];
    }
  }


  /**
   * Util Function to getMenuContent pool list and status of Pool
   * @namespace xio.PoolsListComponent
   * @param {any} ise_id
   * @method getPoolsList
   * @return {void}
   */
  getPoolsList(ise_id: number) {
    this.store.dispatch(new GetAllPoolsAction(this.ise_id));
    this.all_pools_state_obs$ = this.store.select(getAllPoolsState)
      .subscribe((data: Array<Pools>) => {
        this.loading_stack.pool_list = false;
        this.pools_list = [];
        let i = 0;
         if (!this.isEmpty(data)) {
           for (let poolData of data) {
                let pool_grid_data = [],
                    media = poolData['media']['media'] ?
                            poolData['media']['media'] :
                            [poolData['media']['medium']];
                    poolData['gridOptions'] = Object.assign({}, poolsListOptions);
                    this.pools_datapac_list[i] = [];
                    this.poolGridOptions[poolData['globalid']] = poolData['gridOptions'];
                    for (let mediaObj of media) {
                       let d_id = mediaObj._attr.self.split('/').pop(),
                           pd = {
                              id: d_id,
                              show: true
                           };
                        if (this.datapac_list[d_id] !== undefined) {
                            pool_grid_data = pool_grid_data.concat(this.datapac_list[d_id].drive);
                        }
                      this.pools_datapac_list[i].push(pd);
                    }

                    for (let index = 0; index < pool_grid_data.length; index++) {
                        if ( pool_grid_data[index]['status'] &&
                             pool_grid_data[index]['status'].hasOwnProperty('_attr')) {
                             pool_grid_data[index]['status'] = pool_grid_data[index]['status']['_attr']['string'];
                        } else if (pool_grid_data[index]['status'] &&
                                   pool_grid_data[index]['status'].hasOwnProperty('detail')) {
                            pool_grid_data[index]['status'] = pool_grid_data[index]['status']['detail'];
                        }

                        // Seting status for toggle button
                        pool_grid_data[index]['toggle'] = ( pool_grid_data[index]['statusleds']
                                        && pool_grid_data[index]['statusleds']['blue']['_attr']['string'] === 'blinking' )
                                        ? true
                                        : false;
                   }

              poolData['gridOptions']['rowData'] = [];
              poolData['gridOptions']['rowData'] = pool_grid_data;
              poolData['driveStatus'] = '';
            let driveStatus = '';
            if (poolData['status'] && poolData['status'].details &&
                poolData['status']['details'].hasOwnProperty('detail')) {
                poolData['isReady'] = poolData['status'] &&
                poolData['status'].details && ( poolData['status'].details.detail === 'None' ||
                poolData['status'].details.detail === 'Uninitialized' ||
                poolData['status'].details.detail === 'Spare capacity could be improved' ||
                poolData['status'].details.detail === 'Drives need replacement' ||
                poolData['status'].details.detail === 'Volume Inoperative' ||
                poolData['status'].details.detail === 'Running out of capacity');
                poolData['driveStatus'] = poolData['status'].details.detail;
            } else if (poolData['status'] && poolData['status'].details &&
                     poolData['status']['details'].hasOwnProperty('details')) {
                     poolData['status']['details']['details']
                       .forEach(function(statusObj) {
                         poolData['isReady'] = statusObj === 'None' ||
                            statusObj === 'Uninitialized' ||
                            statusObj === 'Spare capacity could be improved' ||
                            statusObj === 'Drives need replacement' ||
                            statusObj === 'Volume Inoperative' ||
                            statusObj === 'Running out of capacity';
                          driveStatus += statusObj + ',';
            });
            driveStatus = driveStatus.replace(/,\s*$/, '');
            poolData['driveStatus'] = driveStatus;
          };
          this.pools_list.push(poolData);
          i++;
        }
      }
    });
  }



  /**
   * Delete Pool controller
   * @namespace xio.PoolsListComponent
   * @param {any} pool_id - ID of the Pool to be deleted
   * @method deletePool
   * @return {void}
   */
  deletePool(poolObj) {
    let dialogRef = this.dialog.open(XioDialogComponent);
        dialogRef.componentInstance.title = 'Delete Pool';
        dialogRef.componentInstance.message = 'Do you really want to delete  ' + poolObj.name + ' ?';
        dialogRef.afterClosed().subscribe(result => {
        if (result === 'yes') {
          this.progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
          this.progressRef.componentInstance.progress_data = 'Loading....';
          let payLoad = {
            pool_id: poolObj.globalid,
            ise_id: this.ise_id,
            cb: this.onPoolDeleteCallBack
          };
          this.store.dispatch(new DeletePoolAction(payLoad));
        }
    });
  }

  /**
   * Util Function to getMenuContent Led Class
   * @namespace xio.PoolsListComponent
   * @param {string} color
   * @method getLedClass
   * @return {string} color
   */
  getLedClass(data: any, color: string): string {
    if (data && data.statusleds) {
      let _strColor = data.statusleds[color]._attr.string;
      return data.statusleds[color]._attr.string === 'on' ?
             color : (_strColor === 'off' ?
            'grey' :
            (color + ' blinking'));
    }
    return 'grey';
  }

  /**
   * Util Function to enable/disable the Identify of Drives
   * @namespace xio.PoolsListComponent
   * @param {any} data - Drives data
   * @param {string} color
   * @method enableDriveLed
   * @return {string} color
   */

  enableDriveLed( data, color ) {
    for ( let data_pac_position in this.drive_track_list ) {
      if ( this.drive_track_list[data_pac_position] ) {       
        for (let data_packs of  this.drive_track_list[data_pac_position]){
          data_packs.forEach(dat_pack => {
            if ( dat_pack['position'] ===  data['rowObject']['position']) {
                let ledColor =  data['led']  === 'enabled' ? color : 'grey';
                if (ledColor === 'blue') {
                dat_pack['statusleds'][color]._attr.string  = 'blinking';                       
                  return true;
                } else {
                dat_pack['statusleds'][color]._attr.string  = 'off';
                  return true;
                } 
              }
          });
        }
          
      }
    }    
    
  }
   
  /**
   * Method will be called on click of identify
   * button in the grid.
   * @param arg
   */
  drivesLed(arg) {
    this.store.dispatch(new UpdateDrivesIdentifyAction({
      ise_id: this.ise_id,
      drive_id: arg.rowObject.position,
      data: { 'led': arg.led },
      cb: (data, error) => {
        if (!error) {            
            // Enable the particular drive            
            this.enableDriveLed(arg , 'blue' );
        } else {
          this.catchError( error );
       }
      }
    }));

  }

    /**
   * catching Error and displaying in Popup
   * @namespace xio.PoolsListComponent
   * @param {any} _error
   * @method catchError
   */

  catchError (_error) {
    if (_error.status === 401) {
      let path = '/ise/' + this.ise_id + '/set-password/';
      this.router.navigate([path]);
    }
    let err_msg = (_error.json !== '' || _error.json !== undefined
      || _error.json !== null) ? _error.json() : '';
    let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
    alertRef.componentInstance.title = 'Pools';
    alertRef.componentInstance.message = err_msg !== '' ?
      err_msg.result.error.message :
      'Bad Request';
  }


  ngOnDestroy() {
    this.store.dispatch(new Reset());
    this.pools_list = [];
    if (this.all_pools_state_obs$) {
      this.all_pools_state_obs$.unsubscribe();
    }
    // Un binding listeners
    window.removeEventListener('click', this.deletePool.bind(this), false);
  }

}
