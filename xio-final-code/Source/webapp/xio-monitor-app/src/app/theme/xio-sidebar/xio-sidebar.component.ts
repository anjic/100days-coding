import {Component, OnInit, OnDestroy} from '@angular/core';
import {Router} from '@angular/router';
import {MenuContentService} from './../services/menu-content.service';
import {modulesRoutes} from './config';
import {Store} from '@ngrx/store';
import {getHostData, getMenuData, getSanGroupLst, State} from '../../reducers/';
import {GetMenuAction, GetMenuHostAction} from '../../actions/menu.action';
import {GetAllAction} from '../../actions/sangroup.action';

@Component({
  selector: 'xio-sidebar',
  templateUrl: './xio-sidebar.component.html',
  styleUrls: ['./xio-sidebar.component.scss']
})
export class XioSidebarComponent implements OnInit, OnDestroy {
  public menu_content: any = [];
  public modulesRoutes: Array<Object>;
  public highLightIndex: any;
  public selectedIse: any;
  public selectedHost: any;
  public menu$;
  public host$;
  public iseHostMap: Object = {};
  public loadingSan: boolean ;
  public multiple = 'multiple';

  constructor(public router: Router,
              public mcs: MenuContentService,
              public store: Store<State>) {
    this.modulesRoutes = modulesRoutes;
    this.loadingSan = false;
  }

  ngOnInit() {

    // subscribe Menu Content with San-group and corresponding ISE
    // this.menu$ = this.store.select(getSanGroupLst).subscribe(
    this.store.dispatch(new GetMenuAction({}));
    this.menu$ = this.store.select(getMenuData).subscribe(
      data => {
        if (data.length > 0) {
          for (var k = 0; k < data.length; k++) {
            if (data[k].hasOwnProperty('ise')) {
              data[k]['ise'].sort(this.compareIse);
              let server_groups = data[k]['server'];
              data[k]['hosts'] = server_groups;
             /* data[k]['ise'].forEach(ise => {
                this.iseHostMap[ise.id] = null;
                data[k]['hosts'] = 'loading';
                console.log(ise);
                this.store.dispatch(new GetMenuHostAction({
                  ise_id: ise.id
                }));
              });*/
            }
          }
          data.sort(this.compare);
        }
        this.menu_content = data;
        //adding highlight flag
        for (let q = 0; q < this.menu_content.length; q++) {
          this.menu_content[q]['highLight'] = false;
        }
      }
    );

    this.host$ = this.store.select(getHostData).subscribe(
      data => {
        if (!this.isEmpty(data)) {
          this.iseHostMap = Object.assign(this.iseHostMap, data);
          this.menu_content.forEach((menu) => {
            if (Array.isArray(menu['hosts']) && menu['hosts'].length > 0)
              menu['hosts'] = [];
            if(menu['ise'] && menu['ise'].length > 0){
              menu['ise'].forEach((ise) => {
                if (this.iseHostMap[ise.id] && this.iseHostMap[ise.id].length > 0) {
                  if (menu['hosts'] == 'loading')
                    menu['hosts'] = [];
                  menu['hosts'] = [...menu['hosts'], ...this.iseHostMap[ise.id]];
                }
              });
            }
            if (Array.isArray(menu['hosts']))
              menu['hosts'].sort(this.compareHost);
            else
              menu['hosts'] = [];
          });
        }
      }
    );


    this.store.dispatch(new GetAllAction({
      cb: () => {
        this.loadingSan = false;
      }
    }));
  }

  loadHostInfo(id) {
    this.mcs.getHostLst({ise_id: id})
      .subscribe(
        data => {
          this.iseHostMap['9'] = data.length > 0 ? data : 'No Data';
        }
      );
  }

  findPathByObject(routeObj) {
    if (routeObj.route === this[0]) {
      return routeObj;
    }
  }

  enableRoute(obj) {
    let index = this.modulesRoutes.findIndex(routeOb => routeOb['route'] === obj.route);
    this.highLightIndex = index;
    for (let k = 0; k < this.modulesRoutes.length; k++) {
      if (index === k) {
        this.modulesRoutes[k]['highLight'] = true;
      } else {
        this.modulesRoutes[k]['highLight'] = false;
      }
    }
  }

  /**
   * Disable main module routes
   */
  disableMainModuleRoute() {
    for (let k = 0; k < this.modulesRoutes.length; k++) {
      this.modulesRoutes[k]['highLight'] = false;
    }
  }

  /**
   * This method disable active ise
   */
  disableActiveIse() {
    for (let k = 0; k < this.menu_content.length; k++) {
      var iseList = this.menu_content[k];
      for (let n = 0; n < iseList['ise'].length; n++) {
        var iseObj = iseList['ise'][n];
        iseObj['highLight'] = false;
      }
    }
  }

  /**
   * This method disable active host
   */
  disableActiveHost() {
    for (let k = 0; k < this.menu_content.length; k++) {
      var hostsList = this.menu_content[k];
      if (hostsList) {
        if (hostsList['hosts'] instanceof Array && hostsList['hosts'].length > 0) {
          for (let n = 0; n < hostsList['hosts'].length; n++) {
            var hostObj = hostsList['hosts'][n];
            hostObj['highLight'] = false;
          }
        }
      }
    }
  }

  /**
   * Navigate to specified path on
   * click of side bar link
   * @param event
   * @param path
   */
  navigateTo(event: any, path: string) {
    event.stopPropagation();
    let routeObj = this.modulesRoutes.find(this.findPathByObject, [path]);
    this.enableRoute(routeObj);
    this.disableAllAccordions();
    this.disableActiveIse();
    this.disableActiveHost();
    this.router.navigate(['/' + path]);
  }

  /**
   * Navigate to Ise Dashboard
   * after click on ISE click
   * @param event
   * @param path
   */
  navigateToIse(event: any, path: any) {
    event.stopPropagation();
    this.router.navigate(['/' + path]);
  }

  /**
   * Open accord for ISE'S
   * @param tab
   */
  openAccord(event, item) {
    //event.stopPropagation();
    this.disableMainModuleRoute();
    this.applyAccordHeader(item);
    this.disableOtherAccordHeaders(item);
    this.disableAllHosts();
    this.disableAllISES();
    //let event = tab.originalEvent;
    //let path = 'san-group/' + this.menu_content[tab.index].sangroup_id + '/dashboard/';
    let path = 'san-group/' + item.sangroup_id + '/dashboard/';
    this.navigateToIse(event, path);
  }

  applyAccordHeader(item:any){
    item['highLight'] = true;
  }

  disableOtherAccordHeaders(item:any){
    for (let k = 0; k < this.menu_content.length; k++) {
      let itemsAccord = this.menu_content[k];
      if (itemsAccord.sangroup_name != item.sangroup_name) {
        itemsAccord['highLight'] = false;
      }
    }
  }

  disableAllAccords(){
    for (let k = 0; k < this.menu_content.length; k++) {
      let itemsAccord = this.menu_content[k];
      itemsAccord['highLight'] = false;
    }
  }

  disableAllAccordions(){
    for (let k = 0; k < this.menu_content.length; k++) {
      let itemsAccord = this.menu_content[k];
      itemsAccord['highLight'] = false;
    }
  }

  disableAllHosts() {
    for (let k = 0; k < this.menu_content.length; k++) {
      let hostList = this.menu_content[k];
      if (hostList && hostList['hosts'] instanceof Array && hostList['hosts'].length > 0) {
        for (let n = 0; n < hostList['hosts'].length; n++) {
          let hostObj = hostList['hosts'][n];
          hostObj['highLight'] = false;
        }
      }
    }
  }

  disableAllISES() {
    for (let k = 0; k < this.menu_content.length; k++) {
      var iseList = this.menu_content[k];
      for (let n = 0; n < iseList['ise'].length; n++) {
        var iseObj = iseList['ise'][n];
        iseObj['highLight'] = false;
      }
    }
  }

  /**
   * Navigate to specified host on click
   * of host in the side bar
   * @param event
   * @param sg_id
   * @param ise_id
   * @param host_id
   */
  goToHost(event: any, allHosts: any, selHost: any, selItem: any) {
    event.stopPropagation();

    //Applying host for host
    for (let k = 0; k < allHosts.length; k++) {
      allHosts[k]['highLight'] = false;
    }
    this.applyAccordHeader(selItem);
    this.enableHostActive(allHosts, selHost);
    //Pending logic to this need to implement
    this.disableOtherGroupHosts(selItem);
    this.disableActiveIse();
    this.disableMainModuleRoute();
    this.disableAllAccords();
    this.applyAccordHeader(selItem);
    this.router.navigate(['/san-group/' + selItem.sangroup_id + '/ise/' + selHost.ise_id + '/host/' + selHost.host_id]);
  }

  /**/
  goToServerGroup(event: any, host_item:any, serverId :any , allHosts: any, selHost: any, selItem: any) {
    event.stopPropagation();

    console.log("selItem..:", selItem);
    for (let k = 0; k < allHosts.length; k++) {
      allHosts[k]['highLight'] = false;
    }

    this.enableHostActive(allHosts, host_item);
    this.disableOtherGroupHosts(selItem);
    this.disableActiveIse();
    this.disableMainModuleRoute();
    this.disableAllAccords();
    this.applyAccordHeader(selItem);
    this.router.navigate(['/server/' + serverId + '/edit/' + '/serverwwn/'+selItem.sangroup_id]);
  }
  /**
   * This method disables other
   * hosts group
   * @param selItem
   */
  disableOtherGroupHosts(selItem: any) {
    for (let k = 0; k < this.menu_content.length; k++) {
      var hostList = this.menu_content[k];
      if (hostList.sangroup_id != selItem.sangroup_id) {
        if (hostList && hostList['hosts'] instanceof Array && hostList['hosts'].length > 0) {
          for (let n = 0; n < hostList['hosts'].length; n++) {
            var hostObj = hostList['hosts'][n];
            hostObj['highLight'] = false;
          }
        }
      }
    }
  }

  /**
   * This method enables active host
   * @param allHosts
   * @param selHost
   */
  enableHostActive(allHosts: any, selHost: any) {
    if (selHost['server_id'] != null &&
      selHost['server_id'] != undefined &&
      selHost['server_id'] != '') {
      this.selectedHost = selHost;
      let index = allHosts.findIndex(hostObj => hostObj['server_id'] === selHost['server_id']);
      for (let q = 0; q < allHosts.length; q++) {
        if (index === q) {
          allHosts[q]['highLight'] = true;
        } else {
          allHosts[q]['highLight'] = false;
        }
      }
    }
  }

  /**
   * This method enables active ise
   * @param allIses
   * @param selIse
   */
  enableIseActive(allIses: any, selIse: any) {
    if (selIse['ise_name'] != null &&
      selIse['ise_name'] != undefined &&
      selIse['ise_name'] != '') {
      this.selectedIse = selIse;
      let index = allIses.findIndex(iseObj => iseObj['ise_name'] === selIse['ise_name']);
      for (let q = 0; q < allIses.length; q++) {
        if (index === q) {
          allIses[q]['highLight'] = true;
        } else {
          allIses[q]['highLight'] = false;
        }
      }
    }
  }

  /**
   * Method disable selected ise
   * @param selItem
   */
  disableOthersIse(selItem: any) {
    for (let k = 0; k < this.menu_content.length; k++) {
      var iseList = this.menu_content[k];
      if (iseList.sangroup_id != selItem.sangroup_id) {
        for (let n = 0; n < iseList['ise'].length; n++) {
          var iseObj = iseList['ise'][n];
          iseObj['highLight'] = false;
        }
      }
    }
  }


  /**
   * this method particular ise dashboard
   * @param event
   * @param ises
   * @param selIseObj
   * @param selItem
   */
  navigateToISEDashBoard(event: any, ises: any, selIseObj: any, selItem: any) {
    event.stopPropagation();

    //Adding property highlight
    for (let k = 0; k < ises.length; k++) {
      ises[k]['highLight'] = false;
    }
    this.enableIseActive(ises, selIseObj);
    this.disableOthersIse(selItem);
    this.disableActiveHost();
    this.disableMainModuleRoute();
    this.disableAllAccords();
    this.applyAccordHeader(selItem);
    this.router.navigate(['/ise/' + selIseObj.id + '/dashboard']);
  }

  isEmpty(obj) {
    return (obj && (Object.keys(obj).length === 0));
  }

  compare(objPrim, objSec) {

    const objA = objPrim.sangroup_name.toUpperCase();
    const objB = objSec.sangroup_name.toUpperCase();

    let comparison = 0;
    if (objA > objB) {
      comparison = 1;
    } else if (objA < objB) {
      comparison = -1;
    }
    return comparison;
  }

  compareHost(objPrim, objSec) {
    const objA = objPrim.hosts.toUpperCase();
    const objB = objSec.hosts.toUpperCase();

    let comparison = 0;
    if (objA > objB) {
      comparison = 1;
    } else if (objA < objB) {
      comparison = -1;
    }
    return comparison;
  }

  compareIse(objPrim, objSec) {
    const objA = objPrim.ise_name.toUpperCase();
    const objB = objSec.ise_name.toUpperCase();

    let comparison = 0;
    if (objA > objB) {
      comparison = 1;
    } else if (objA < objB) {
      comparison = -1;
    }
    return comparison;
  }

  gotToHosts(event, sanGrpId) {
    event.stopPropagation();
    this.router.navigate(['/san-group/' + sanGrpId + '/host']);
  }

  ngOnDestroy() {
    this.menu$.unsubscribe();
    this.host$.unsubscribe();
  }
}
