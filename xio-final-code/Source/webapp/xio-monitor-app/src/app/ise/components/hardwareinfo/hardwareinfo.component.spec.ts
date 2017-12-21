import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HardwareinfoComponent } from './hardwareinfo.component';

describe('HardwareinfoComponent', () => {
  let component: HardwareinfoComponent;
  let fixture: ComponentFixture<HardwareinfoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HardwareinfoComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HardwareinfoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
