import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HostEditButtonComponent } from './host-edit-button.component';

describe('HostEditButtonComponent', () => {
  let component: HostEditButtonComponent;
  let fixture: ComponentFixture<HostEditButtonComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HostEditButtonComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HostEditButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
