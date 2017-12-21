import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IseChangePwdComponent } from './changepwd.component';

describe('IseChangepwdComponent', () => {
  let component: IseChangePwdComponent;
  let fixture: ComponentFixture<IseChangePwdComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IseChangePwdComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IseChangePwdComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
