import { TestBed, inject } from '@angular/core/testing';

import { IseService } from './ise.service';

describe('IseService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [IseService]
    });
  });

  // it('should ...', inject([IseService], (service: IseService) => {
  //   expect(service).toBeTruthy();
  // }));
});
