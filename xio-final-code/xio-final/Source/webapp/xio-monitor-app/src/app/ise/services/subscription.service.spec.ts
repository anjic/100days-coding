import { TestBed, inject } from '@angular/core/testing';

import { SubscriptionService } from './subscription.service';

describe('SubscriptionService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [SubscriptionService]
    });
  });

  // it('should ...', inject([SubscriptionService], (service: SubscriptionService) => {
  //   expect(service).toBeTruthy();
  // }));
});
