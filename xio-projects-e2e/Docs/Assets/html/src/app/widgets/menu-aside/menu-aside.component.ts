import { Component, OnInit } from '@angular/core';
import { User } from '../../models/user';
import { Router } from '@angular/router';
import { UserService } from '../../services/user.service';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-menu-aside',
  styleUrls: ['./menu-aside.component.css'],
  templateUrl: './menu-aside.component.html'
})
export class MenuAsideComponent implements OnInit {
  private currentUrl: string;
  private links: Array<any> = [
    {
      'title': 'Dashboard',
      'icon': 'desktop',
      'link': ['/']
    },
    {
      'title': 'SAN Groups',
      'icon': 'folder',
      'link': ['/page/1']
    },
    {
      'title': 'ISEs',
      'icon': 'hdd-o',
      'link': ['/pages/new/']
    },
    {
      'title': 'User Management',
      'icon': 'universal-access',
      'sublinks': [
        {
          'title': 'Users',
          'icon': 'user',
          'link': ['/page/2'],
        },
        {
          'title': 'Groups',
          'icon': 'users',
          'link': ['/page/3'],
        },
        {
          'title': 'Access Control',
          'icon': 'unlock',
          'link': ['/page/1'],
        }
      ]
    },
    {
      'title': 'Performance',
      'icon': 'bar-chart-o',
      'sublinks': [
        {
          'title': 'SAN Group',
          'icon': 'folder',
          'link': ['/page/2'],
        },
        {
          'title': 'ISE',
          'icon': 'hdd-o',
          'link': ['/page/3'],
        }
      ]
    },
    {
      'title': 'Logs',
      'icon': 'file',
      'link': ['/page/new'],
      
    }
    
  ];

  constructor(private userServ: UserService, public router: Router, private auth: AuthService) {
    // getting the current url
    this.router.events.subscribe((evt) => this.currentUrl = evt.url);
  }

  public ngOnInit() {
    // TODO
  }

}
