import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { VolumeEditButtonComponent } from './volume-edit-button.component';

describe('VolumeEditButtonComponent', () => {
  let component: VolumeEditButtonComponent;
  let fixture: ComponentFixture<VolumeEditButtonComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ VolumeEditButtonComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(VolumeEditButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
