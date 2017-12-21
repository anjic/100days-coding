import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IseDeleteButtonComponent } from './delete-button.component';

describe('IseDeleteButtonComponent', () => {
  let component: IseDeleteButtonComponent;
  let fixture: ComponentFixture<IseDeleteButtonComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IseDeleteButtonComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IseDeleteButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
