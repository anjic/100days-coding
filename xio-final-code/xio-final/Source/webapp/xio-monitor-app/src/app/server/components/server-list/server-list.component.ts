import { Component, OnInit, OnDestroy } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { serverListConfig } from "./server-list-options";
import { GridOptions } from "../../../common/Metadata/xio.dataTable";
import { Store } from '@ngrx/store';
import { State } from '../../../reducers/';
import { Observable } from 'rxjs/Observable';
import { getServerLstState } from '../../../reducers/index';
import { GetAllAction , DeleteServerAction } from '../../../actions/server.actions';
import { XioDialogComponent } from "../../../theme/xio-dialog/xio-dialog.component";
import { MdDialog } from "@angular/material";
import { XioProgressComponent } from "../../../theme/xio-progress/xio-progress.component";
import { XioAlertComponent } from "../../../theme/xio-alert/xio-alert.component";
import { SnackbarService } from "../../../theme/services/snackbar.service";
import {GetMenuAction} from "../../../actions/menu.action";

@Component({
  selector: 'app-server-list',
  templateUrl: './server-list.component.html',
  styleUrls: ['./server-list.component.scss']
})
export class ServerListComponent implements OnInit,OnDestroy {
  public gridOptions;
  public server_list: any;
  public columnDefs: any;
  public server$;

  constructor(public router: Router,
    public store: Store<State>,
    public dialog: MdDialog,
    public snackbarService: SnackbarService) {

    // this.store.dispatch(new GetAllAction());
  }


  ngOnInit() {
    this.gridOptions = serverListConfig;
    this.gridOptions['deleteCb'] = this.bindServerDeleteCb.bind(this);
    this.store.dispatch(new GetAllAction());
    this.server$ = this.store.select(getServerLstState).subscribe(
      res => {
        if(res && res.length > 0 && Array.isArray(res)){
          this.gridOptions.rowData = res;
        } else if(res && res.length == 0){
           this.gridOptions.rowData = res;
        }
      });
  }



  navigateTo(event: any, path: string) {
    event.stopPropagation();
    this.router.navigate([path]);
  }

  bindServerDeleteCb(data) {
    let that = this;
    const ser_name = data.server_name,
      dialogRef = this.dialog.open(XioDialogComponent);

    dialogRef.componentInstance.title = 'Delete Server';
    dialogRef.componentInstance.message = 'Do you want to Delete ' + ser_name + ' Server';
    dialogRef.afterClosed().subscribe(result => {

      if (result === 'yes') {
        const progressRef = this.dialog.open(XioProgressComponent, { disableClose: true });
        progressRef.componentInstance.progress_data = 'Loading....';
        this.store.dispatch(new DeleteServerAction({
          server_id: data.server_id,
          cb: (res, err) => {
            if (!err) {
              progressRef.close();
              this.gridOptions.rowData = this.gridOptions.rowData.filter(d => {
                if (d.server_id != res.server_id) {
                  return d;
                }
              });
              this.snackbarService.toastMe('Server Deleted Successfully', 2000);
              this.store.dispatch(new GetAllAction());
              this.store.dispatch(new GetMenuAction({}));
            } else {
              progressRef.close();
              let err_msg = err.json();
              let alertRef = that.dialog.open(XioAlertComponent, { disableClose: true });
              alertRef.componentInstance.title = 'Server';
              alertRef.componentInstance.message = err_msg.result.error.message;
            }
          }
        }));
      }

    });
  }

  ngOnDestroy(){

  }


}
