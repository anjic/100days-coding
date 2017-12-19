import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {Router} from '@angular/router';
import {AuthService} from './../../auth/services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  public loginForm: any;
  public error: boolean;
  public error_msg: string;
  public ise_id:any;

  constructor(public fb: FormBuilder, public auths: AuthService, public router: Router) {
    if (auths.getToken()) {
      this.router.navigate(['/ise']);
    }
  }

  ngOnInit() {
    this.loginForm = this.fb.group({
      'user_name': ['Administrator', Validators.required],
      'password': ['', Validators.required]
    });

  }

  /**
   * Authenticate User by user name and pwd
   * @namespace xio.LoginComponent
   * @method doLogin
   * @return {void}
   */
  doLogin() {
    this.error = false;
    this.error_msg = '';
    this.auths.login(this.loginForm.value.user_name, this.loginForm.value.password).subscribe(
      (res) => {
        console.log(res);
        if(res && res.user_privilege)
        this.ise_id=res.user_privilege.prefered_ise;
        if (res) {
          sessionStorage.setItem('currentUser', JSON.stringify({ username: res.username, token: res.token }));
          this.router.navigate(['/ise/'+ this.ise_id +'/dashboard']);
          this.auths.is_login = !!res.token;
        }
       if(!this.ise_id){
         console.log("***********")
         this.router.navigate(['/ise/list']);
       }
      },
      err => {
        const e = err.json();
        this.error = true;
        this.error_msg = e.result.error.message;
      }
    );
  }
}
