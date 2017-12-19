import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';

@Component({
  selector: 'app-refresh-button',
  templateUrl: './refresh-button.component.html',
  styleUrls: ['./refresh-button.component.scss']
})
export class RefreshButtonComponent implements OnInit {

  @Input() screen_name: any;
  @Output() onRefreshClick: EventEmitter<any> = new EventEmitter<any>();

  constructor() { }

  ngOnInit() {
  }

  refreshCurrentScreen(event) {
    switch ( this.screen_name ) {
      case 'dashboard':
             this.onRefreshClick.emit('dashboard');
             break;
      case 'performance':
            this.onRefreshClick.emit('performance');
            break;
    }

  }

}
