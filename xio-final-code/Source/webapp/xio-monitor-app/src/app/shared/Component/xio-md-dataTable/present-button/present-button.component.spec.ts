import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IsePresentButtonComponent } from './present-button.component';

describe('IsePresentButtonComponent', () => {
  let component: IsePresentButtonComponent;
  let fixture: ComponentFixture<IsePresentButtonComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IsePresentButtonComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IsePresentButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
