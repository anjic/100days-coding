import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SetIsePasswordComponent } from './set-ise-password.component';

describe('SetIsePasswordComponent', () => {
  let component: SetIsePasswordComponent;
  let fixture: ComponentFixture<SetIsePasswordComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SetIsePasswordComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SetIsePasswordComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
