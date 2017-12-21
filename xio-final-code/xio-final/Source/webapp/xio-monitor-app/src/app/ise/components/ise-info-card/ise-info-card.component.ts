import {Component, Input, OnInit} from '@angular/core';
import {Router} from "@angular/router";

@Component({
  selector: 'app-ise-info-card',
  templateUrl: './ise-info-card.component.html',
  styleUrls: ['./ise-info-card.component.scss']
})
export class IseInfoCardComponent implements OnInit {

  @Input() ise;
  
  public status:string;

  constructor(public router: Router) {}

  ngOnInit() {
     this.status=this.ise.status
   }
  getStatus(status:string):string {
    if(status == 'Operational'){
      return 'san-dashboard-ise-cards-operational';
    }
    else if(status == 'Warning'){
      return 'san-dashboard-ise-cards-warning';
    }
    else {
      return 'san-dashboard-ise-cards-critical';
    }
  }

  onClick(ise_id) {
    this.router.navigate(['/ise/' + ise_id + '/dashboard']);
  }
}
