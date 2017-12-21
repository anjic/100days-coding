import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { XioAlertComponent } from './xio-alert.component';

describe('XioAlertComponent', () => {
  let component: XioAlertComponent;
  let fixture: ComponentFixture<XioAlertComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ XioAlertComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(XioAlertComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
