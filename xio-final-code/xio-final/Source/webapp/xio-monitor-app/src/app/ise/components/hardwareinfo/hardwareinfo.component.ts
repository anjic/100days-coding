import { Component, OnInit , OnDestroy } from '@angular/core';
import { Router, ActivatedRoute, Params } from '@angular/router';
import { SharedDataService } from './hardware-tabs/shared-data.service';


@Component({
  selector: 'app-hardwareinfo',
  templateUrl: './hardwareinfo.component.html',
  styleUrls: ['./hardwareinfo.component.scss'],
  providers: [ SharedDataService ]
})
export class HardwareinfoComponent implements OnInit, OnDestroy {

  public ise_id;
  public selectedIndex;
  public loading_stack;
  public tabs: any = [
    'mrc',
    'opendatapac',
    'powersupply',
    'network',
    'fans'
  ];


  /**
  * @param {ActivatedRoute} activatedRoute
  * @param {SharedDataService} _sharedDataService
  * @param {Router} router
  */

  constructor(public activatedRoute: ActivatedRoute,
              public _sharedDataService: SharedDataService,
              public router: Router) {
          this.selectedIndex = 0;
          this.loading_stack = {
              hardinfo_details: false,
              hardinfo_details_text: 'Loading.....'
          };
  }

  ngOnInit() {
    this.activatedRoute.parent.params.subscribe(params => {
        this.selectedIndex = this.tabs.indexOf(this.router.url.split('/')[4]);
        this.ise_id = params['ise_id'];
        this._sharedDataService._data.next(this.ise_id);
    });
  }

  /**
   * Desc : change tab click event
   * @namespace xio.IseLandingComponent
   * @method changeTab
   * @param {Object} e - event
   * @return {void}
   **/

  changeTab(e) {
    if (this.tabs[e.index]) {
      let url = '/ise/' + this.ise_id + '/hardwareinfo/' + this.tabs[e.index];
      this.router.navigateByUrl(url);
    }
  }


  ngOnDestroy() {
    // Unbinding listerners
    window.removeEventListener('focuschange', this.changeTab.bind(this), false);
  }


}
