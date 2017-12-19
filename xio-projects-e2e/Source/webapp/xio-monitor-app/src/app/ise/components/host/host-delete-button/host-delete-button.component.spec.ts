import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HostDeleteButtonComponent } from './host-delete-button.component';

describe('HostDeleteButtonComponent', () => {
  let component: HostDeleteButtonComponent;
  let fixture: ComponentFixture<HostDeleteButtonComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HostDeleteButtonComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HostDeleteButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
