import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IseEditButtonComponent } from './edit-button.component';

describe('IseEditButtonComponent', () => {
  let component: IseEditButtonComponent;
  let fixture: ComponentFixture<IseEditButtonComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IseEditButtonComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IseEditButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
