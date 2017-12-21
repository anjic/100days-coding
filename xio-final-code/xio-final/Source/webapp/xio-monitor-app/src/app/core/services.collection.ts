import {IseService} from './../ise/services/ise.service';
import {UserService} from '../user/services/user.service';
import {SangroupService} from '../san-group/services/sangroup.service';
import {MenuContentService} from './../theme/services/menu-content.service';
import {StoragevolumeService} from './../ise/services/storagevolume.service';
import {HostService} from './../ise/services/host.service';
import {PoolsService} from './../ise/services/pools.service';
import {AuthService} from './../auth/services/auth.service';
import {AuthGuard} from './../auth/services/auth.guard';
import {SnackbarService} from './../theme/services/snackbar.service';
import {IseSettingService} from '../ise/services/ise-setting.service';
import {EndpointsService} from './../ise/services/endpoints.service'
import {SubscriptionService} from './../ise/services/subscription.service';
import {EmailService} from './../ise/services/email.service';
import {MrcService} from './../ise/services/mrc.service';
import {ServermanagementService} from './../server/service/servermanagement.service';

export const ALL_SERVICES = [
  AuthGuard,
  AuthService,
  IseService,
  SangroupService,
  UserService,
  MenuContentService,
  StoragevolumeService,
  HostService,
  PoolsService,
  SnackbarService,
  IseSettingService,
  EndpointsService,
  EmailService,
  SubscriptionService,
  MrcService,
  ServermanagementService
];
