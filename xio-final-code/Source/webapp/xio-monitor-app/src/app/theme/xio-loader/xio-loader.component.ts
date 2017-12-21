import {Component, OnInit, Input} from '@angular/core';

@Component({
  selector: 'app-xio-loader',
  templateUrl: './xio-loader.component.html',
  styleUrls: ['./xio-loader.component.scss']
})
export class XioLoaderComponent implements OnInit {
  @Input() displayText;

  constructor() {
  }

  ngOnInit() {
  }

}
