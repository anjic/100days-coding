import {Component, OnInit} from '@angular/core';
import {ActivatedRoute,Router} from '@angular/router';
import {listConfig} from './endpoint-list-options';
import {GridOptions} from "./../../../../common/Metadata/xio.dataTable";
import {EndpointsService} from './../../../services/endpoints.service';
import {HostService} from './../../../services/host.service';

@Component({
  selector: 'app-endpoint-list',
  templateUrl: './endpoint-list.component.html',
  styleUrls: ['./endpoint-list.component.scss']
})
export class EndpointListComponent implements OnInit {
  public endpoints_list: any;
  public gridOptions;
  public columnDefs: any;
  public ise_id: number;

  constructor(public eps: EndpointsService,
              public hs: HostService,
              public route: ActivatedRoute,
              public router:Router) {
  
      this.gridOptions = listConfig;
  }


  ngOnInit() {

    this.route.parent.params.subscribe(params => {
      this.ise_id = params['ise_id'];
    });

    this.eps.getAll(this.ise_id).subscribe(
      data => {
        this.endpoints_list = this.eps.endpoint_list;
        var host_wwn = {};
        let payLoad ={
          ise_id:this.ise_id
        }
        this.hs.getAll(payLoad).subscribe(
          res => {
            for (let host of res) {
              let res_data: any = '';
              if (host['endpoints'].hasOwnProperty('endpoints')) {
                res_data = host['endpoints']['endpoints'];
              } else {
                res_data = [host['endpoints']['endpoint']];
              }

              for (let data of res_data) {
                host_wwn[data['globalid']] = host['name'];
              }
            }
            this.eps.endpoint_list.forEach((en) => {
              if (!host_wwn.hasOwnProperty(en.globalid)) {
                host_wwn[en.globalid] = 'Un Assigned';
              }
            });
            this.gridOptions.rowData = Object.keys(host_wwn).map((k) => {
              return {
                "globalid": k,
                "host_name": host_wwn[k]
              }
            });
          },
          err => {
            console.log(err);
          }
        );
      },
      err => {
          if(err && err['status'] == 401){
             let path = '/ise/' + this.ise_id + '/set-password/';
             this.router.navigate([path]);
       }
     });
  }
}
