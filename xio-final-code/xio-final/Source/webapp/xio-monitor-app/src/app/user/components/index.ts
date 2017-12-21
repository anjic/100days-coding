import { UserComponent } from './user/user.component';
import { UserListComponent } from './user-list/user-list.component';
import { UserFormComponent } from './user-form/user-form.component';
import { UserChangepwdComponent } from './user-changepwd/user-changepwd.component';

export const USER_COMPONENTS = [
  UserComponent,
  UserListComponent,
  UserFormComponent,
  UserChangepwdComponent
];

export const USERS_ROUTES = [
  {
    path: '', component: UserComponent,
    children: [
      { path: '', redirectTo: 'list', pathMatch: 'full' },
      { path: 'list', component: UserListComponent },
      { path: 'changepwd-button', component: UserChangepwdComponent },
      { path: 'create', component: UserFormComponent },
      { path: 'edit/:id', component: UserFormComponent }
    ]
  }
];
