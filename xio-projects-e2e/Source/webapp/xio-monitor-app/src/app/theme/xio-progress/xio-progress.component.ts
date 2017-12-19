import {Component, OnInit, Input} from '@angular/core';

@Component({
  selector: 'app-xio-progress',
  templateUrl: './xio-progress.component.html',
  styleUrls: ['./xio-progress.component.scss']
})
export class XioProgressComponent implements OnInit {
  @Input() progress_data;
  color = 'primary';
  mode = 'indeterminate';
  disableClose = true;

  constructor() {
  }

  ngOnInit() {
  }

}
