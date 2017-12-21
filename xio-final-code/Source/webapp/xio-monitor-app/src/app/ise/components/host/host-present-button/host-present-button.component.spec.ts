import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HostPresentButtonComponent } from './host-present-button.component';

describe('HostPresentButtonComponent', () => {
  let component: HostPresentButtonComponent;
  let fixture: ComponentFixture<HostPresentButtonComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HostPresentButtonComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HostPresentButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
