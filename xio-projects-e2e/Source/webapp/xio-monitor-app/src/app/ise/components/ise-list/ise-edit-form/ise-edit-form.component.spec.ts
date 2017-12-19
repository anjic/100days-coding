import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IseEditFormComponent } from './ise-edit-form.component';

describe('IseEditFormComponent', () => {
  let component: IseEditFormComponent;
  let fixture: ComponentFixture<IseEditFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IseEditFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IseEditFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
