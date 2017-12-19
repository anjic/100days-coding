import { TestBed, inject } from '@angular/core/testing';

import { MrcService } from './mrc.service';

describe('MrcService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [MrcService]
    });
  });

  // it('should ...', inject([MrcService], (service: MrcService) => {
  //   expect(service).toBeTruthy();
  // }));
});
