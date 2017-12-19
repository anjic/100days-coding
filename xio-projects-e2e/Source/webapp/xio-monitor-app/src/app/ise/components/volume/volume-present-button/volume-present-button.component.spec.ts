import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { VolumePresentButtonComponent } from './volume-present-button.component';

describe('VolumePresentButtonComponent', () => {
  let component: VolumePresentButtonComponent;
  let fixture: ComponentFixture<VolumePresentButtonComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ VolumePresentButtonComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(VolumePresentButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
