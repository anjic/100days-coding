import {Component, OnInit, ViewChild} from '@angular/core';
import { IopsComponent } from '../../../ise/components/charts/iops/iops.component';
import { DataRateComponent } from '../../../ise/components/charts/data-rate/data-rate.component';
import { LatencyComponent } from '../../../ise/components/charts/latency/latency.component';
import { QueueDepthComponent } from '../../../ise/components/charts/queue-depth/queue-depth.component';

@Component({
  selector: 'app-ise-performance',
  templateUrl: './ise-performance.component.html',
  styleUrls: ['./ise-performance.component.scss']
})
export class IsePerformanceComponent implements OnInit {

  
  @ViewChild('IopsComponent') iopsComponent:IopsComponent;
  @ViewChild('DataRateComponent') dataRateComponent:DataRateComponent;
  @ViewChild('LatencyComponent') latencyComponent:LatencyComponent;
  @ViewChild('QueueDepthComponent') queueDepthComponent:QueueDepthComponent;




  constructor() {
   
  }

  ngOnInit() {
    //Need to implment calls to child components
  }

  loadChild() {
    this.iopsComponent.getData();
    this.dataRateComponent.getData();
    this.latencyComponent.getData();
    this.queueDepthComponent.getData();
  }
  

}
