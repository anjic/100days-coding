import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute,Router } from '@angular/router';
import { FullWidthCellRenderer } from './full-width-cell-renderer.class';
import { VolumeEditButtonComponent } from './volume-edit-button/volume-edit-button.component';
import { VolumeDeleteButtonComponent } from './volume-delete-button/volume-delete-button.component';
import { PoolsService, StoragevolumeService, IseService } from './../../services/';
//Redux
import { Store } from '@ngrx/store';
import { State, getAllVolumesState, getAllPoolsState } from "../../../reducers/";
import { Reset } from "../../../actions/pools.actions";
import { GetAllVolumesAction, DeleteVolumeAction } from "../../../actions/volume.actions";
import { SetISEId } from "../../../actions/ise-management.actions";
import { volumeListConfig } from "./volume-list-options";
import { GridOptions } from "../../../common/Metadata/xio.dataTable";
import { MdDialog } from "@angular/material";
import { XioDialogComponent } from "../../../theme/xio-dialog/xio-dialog.component";
import { XioProgressComponent } from "../../../theme/xio-progress/xio-progress.component";
import { XioAlertComponent } from "../../../theme/xio-alert/xio-alert.component";
import { SnackbarService } from "../../../theme/services/snackbar.service";
import { Subscription } from 'rxjs/Subscription';

interface IVolumeRowData {
  "allocpercent": string;
  "comment": string;
  "alloctype": {"_attr": {"string": string, "value": string}, "alloctype": string};
  "_attr": {"self": string};
  "allocation": {"_attr": {"self": string}, "globalid": string, "hostname": string, "lun": number}[];
  "allocations": {"_attr": {"self": string}, "allocations": {"_attr": {"self": string}, "globalid": string, "hostname": string, "lun": number}[]};
  "affinity": {"_attr": {"string": string, "value": string}, "flashpercent": string};
  "BlocksInBytes": number;
  "MapNumberSheetsAllocated": number;
  "iops": number;
  "host_id": string;
  "id": string;
  "createdate": string;
  "globalid": string;
  "iomap": {"_attr": {"string": string, "value": string}, "iomap": string};
  "configurationpolicy": {"redundancy": {"_attr": {"string": string, "value": string}, "redundancy": string}, "writecache": string};
  "MapNumberWritten": number;
  "IOPSburst": number;
  "productid": string;
  "MapMaxWritten": number;
  "MapEntrySizeInBlocks": number;
  "IOPSmax": number;
  "localid": number;
  "IOPSmin": number;
  "ise_id": string;
  "MapWrittenEntrySizeInBlocks": number;
  "QosStatusStr": string;
  "MapNumberProvisioned": number;
  "MapNumberAllocated": number;
  "pools": {"_attr": {"self": string}, "pool": {"_attr": {"self": string}, "globalid": string, "id": number}};
  "QosStatus": number;
  "mirrors": {"_attr": {"self": string}, "mirrors": string};
  "qosmode": {"_attr": {"string": string, "value": string}, "qosmode": string};
  "name": string;
  "QosSeconds": number;
  "MapSheetMappableEntries": number;
  "MapSheetsSizeInBlocks": number;
  "size": number;
  "snapshots": string;
  "status": {"_attr": {"string": string, "value": string}, "details": {"_attr": {"value": string}, "detail": (string | string[])}};
  "type": string;
  "vendorid": string;
  "volume_id": string;
  "wp": {"_attr": {"string": string, "value": string}, "wp": string}
}

@Component({
  selector: 'app-volume',
  templateUrl: './volume.component.html',
  styleUrls: ['./volume.component.scss'],
  providers: [IseService, StoragevolumeService, PoolsService]
})
export class VolumeComponent implements OnInit, OnDestroy {
  public isAddForm: boolean;
  public columnDefs: any;
  public gridOptions;
  public ise_id: number;
  public volume_list: any;
  public pools_list: any;
  public volumes_list$: Subscription;
  public count = 0;
  public progressRef;

  constructor(public ises: IseService,
    public route: ActivatedRoute,
    public router : Router,
    public svs: StoragevolumeService,
    public ps: PoolsService,
    public store: Store<State>,
    public dialog: MdDialog,
    public snackbarService: SnackbarService) {
  }


  ngOnInit() {
    this.pools_list = { test: 'test' };
    this.gridOptions = Object.assign({}, volumeListConfig);
    this.gridOptions['deleteCb'] = this.bindVolumeDeleteCb.bind(this);
    //this.initGrid();
    this.route.parent.params.subscribe(
      params => {
        this.ise_id = params['ise_id'];
        this.store.dispatch(new SetISEId(this.ise_id));
      });
    this.subcribeVolumeList();
  }

  ngOnDestroy() {
    this.store.dispatch(new Reset());
    if (this.volumes_list$) {
      this.volumes_list$.unsubscribe();
    }
  }

  // UNUSED FUNCTION
  /* getMenuContent status
  * @namespace xio.VolumeComponent
  * @method getstatus
  * @return {void}
  */
  getstatus(params) {
    let status = '';
    if (params.data.status && params.data.status.details) {
      status = params.value + '(' + params.data.status.details.detail + ')';
    }
    return status;
  }

  isEmpty(obj) {
    return (obj && (Object.keys(obj).length === 0));
  }

  removeDuplicates(myArr, prop) {
    // O(n) solution
    var found = {};
    return myArr.reduce((results, currObj) => { // O(n)
      if (!found[currObj[prop]]) {              // O(1)
          found[currObj[prop]] = 1;             // O(1)
          results.push(currObj);                // O(1)
      }
      return results;
    }, []);

    // O(n^2) solution
    // return myArr.filter((obj, pos, arr) => { // O(n)
    //   return arr.map(mapObj => mapObj[prop]) // O(n)
    //             .indexOf(obj[prop]) === pos; // O(n)
    // });
  }

  

  /**
   * getMenuContent Volume list data
   * @namespace xio.VolumeComponent
   * @method subcribeVolumeList
   * @return {void}
   */

  subcribeVolumeList() {
    this.store.dispatch(new GetAllVolumesAction({
      ise_id: this.ise_id,
      cb: (success, error) => {
        if (!error) {
          this.volumes_list$ = this.store.select(getAllVolumesState).subscribe((data:IVolumeRowData[]) => {
            // TODO: Add type definition for data
            if (data) {
              this.volume_list = data; // <-- not used anywhere?
              // TODO: Add type definition for row -- Should not be using bracket notation for 
              // object property access to avoid TypeScript errors
              this.gridOptions.rowData = data.map((row) => {
                let tempAllocations:{lun: number, hostname: string}[] = [], allocatedHost:{lun: number, hostname: string}[] = [];
                let raid, pool, iopsmin: (string | number), iopsmax: (string | number), iopsburst: (string | number), qos, provisioning, status;
                raid = pool = iopsmin = iopsmax = iopsburst = qos = provisioning = status = '';
                iopsmin = row.IOPSmin == 0 ? 'not set' : row.IOPSmin;
                iopsmax = row.IOPSmax == 0 ? 'not set' : row.IOPSmax;
                iopsburst = row.IOPSburst == 0 ? 'not set' : row.IOPSburst;

                if (row && row.alloctype && row.alloctype._attr &&
                  row.alloctype._attr.string) {
                  provisioning = row.alloctype._attr.string;
                }

                if (row && row.status && row.status) {
                  status = row.status._attr.string + '(';
                  if (typeof row.status.details.detail === "string") {
                    status += row.status.details.detail;
                  }
                  else if (typeof row.status.details.detail === "object"
                          && row.status.details.detail.constructor.prototype === Array.prototype) {
                    // take last element
                    status += row.status.details.detail.slice(-1).pop();
                  }
                  status += ')';
                }
                

                if (row && row.configurationpolicy &&
                  row.configurationpolicy.redundancy &&
                  row.configurationpolicy.redundancy._attr &&
                  row.configurationpolicy.redundancy._attr.string) {
                  raid = row.configurationpolicy.redundancy._attr.string;
                }

                if (row && row.pools && row.pools.pool && row.pools.pool.id) {
                  pool = row.pools.pool.id;
                }
                if (row && row.qosmode && row.qosmode._attr && row.qosmode._attr.string) {
                  qos = row.qosmode._attr.string;
                }

                if (row && row.allocation) {
                  tempAllocations = row.allocation.map((alloc) => {
                    return {
                      lun: alloc.lun,
                      hostname: alloc.hostname
                    };
                  });
                  allocatedHost = this.removeDuplicates(tempAllocations, 'hostname');
                }

                return {
                  comment: row.comment,
                  ise_id: this.ise_id,
                  volume_name: row.name,
                  size: row.size,
                  raid: raid,
                  pool: pool,
                  create_date: row.createdate,
                  allocation: row.allocpercent + '' + ('%'),
                  provisioning: provisioning,
                  dedupe_type: row.type,
                  status: status,
                  qos: qos,
                  iopsmin: iopsmin,
                  iopsmax: iopsmax,
                  iopsburst: iopsburst,
                  guiid: row.globalid,
                  allocations: allocatedHost
                };
              });
            }
          }, error => {
            console.log(error);
          });

        } else {
           if (error.status === 401) {
              let path = '/ise/' + this.ise_id + '/set-password/';
              this.router.navigate([path]);
            }

        }
      }
    }));

  }

  /**
   * Renderer Fn for ng-grid cell
   * @namespace xio.VolumeComponent
   * @method poolCellRenderer
   * @return {void}
   */
  poolCellRenderer(params) {
    if (params.value && params.value.id)
      return 'Pool ' + params.value.id;
  }

  bindVolumeDeleteCb(data) {
    let name = data.volume_name;
    let vol_id = data['guiid'];
    let dialogRef = this.dialog.open(XioDialogComponent);
    dialogRef.componentInstance.message = 'Do you really want to delete "' + name + '" ?';
    dialogRef.componentInstance.title = "Delete Volume";
    dialogRef.afterClosed().subscribe(result => {
      if (result == 'yes') {
        this.progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
        this.progressRef.componentInstance.progress_data = "Loading....";
        let payLoad = {
          "ise_id": this.ise_id,
          "id": data.guiid,
          "cb": ((success, error) => {
            if (!error) {
              this.progressRef.close();
              this.progressRef = null;
              this.snackbarService.toastMe('Volume Deleted Successfully', 2000);
              this.gridOptions.rowData = this.gridOptions.rowData.filter(d => {
                if (d['guiid'] != vol_id) {
                  return d;
                }
              });
            } else {
              this.progressRef.close();
              this.progressRef = null;
              let alertRef = this.dialog.open(XioAlertComponent, { disableClose: true });
              alertRef.componentInstance.title = "Volume";
              alertRef.componentInstance.message = error.json().result.error.message;
            }
          })
        };
        this.store.dispatch(new DeleteVolumeAction(payLoad));
      }
    });
  }
}
