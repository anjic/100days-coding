import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IseChangepwdFormComponent } from './ise-changepwd-form.component';

describe('IseChangepwdButtonComponent', () => {
  let component: IseChangepwdFormComponent;
  let fixture: ComponentFixture<IseChangepwdFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IseChangepwdFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IseChangepwdFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
