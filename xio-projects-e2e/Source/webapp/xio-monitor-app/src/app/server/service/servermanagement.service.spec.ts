import { TestBed, inject } from '@angular/core/testing';

import { ServermanagementService } from './servermanagement.service';

describe('ServermanagementService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ServermanagementService]
    });
  });

  it('should be created', inject([ServermanagementService], (service: ServermanagementService) => {
    expect(service).toBeTruthy();
  }));
});
