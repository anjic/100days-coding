import { TestBed, inject } from '@angular/core/testing';

import { SnmpService } from './snmp.service';

describe('SnmpService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [SnmpService]
    });
  });

  // it('should ...', inject([SnmpService], (service: SnmpService) => {
  //   expect(service).toBeTruthy();
  // }));
});
