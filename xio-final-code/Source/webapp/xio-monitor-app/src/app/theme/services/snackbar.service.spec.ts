import { TestBed, inject } from '@angular/core/testing';

import { SnackbarService } from './snackbar.service';

describe('SnackbarService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [SnackbarService]
    });
  });

  // it('should ...', inject([SnackbarService], (service: SnackbarService) => {
  //   expect(service).toBeTruthy();
  // }));
});
