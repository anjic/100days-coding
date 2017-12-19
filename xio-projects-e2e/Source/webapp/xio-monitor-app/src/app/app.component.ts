import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from './auth/services/auth.service';
import { SnackbarService} from './theme/';
@Component({
	selector: 'app-root',
	templateUrl: './app.component.html',
	styleUrls: ['./app.component.scss']
})

export class AppComponent {

	title = '';

	constructor(public auth: AuthService,public router : Router,public snackbarService:SnackbarService) { }

	logout() {
		this.auth.logout();
		this.router.navigate(['/login']);
	}

	changePassword() {
		this.router.navigate(['/user/changepwd-button']);
	}
	contactUs(){
		this.router.navigate(['/contact-us']);
	}

	ngOnInit() {

		let detect= window.navigator.vendor;
		(detect.indexOf('Google')!=-1) ? '' : this.snackbarService.toastMe('Optimized For Chrome', 3000);
			}

}
