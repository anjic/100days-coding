import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { VolumePresentLinkComponent } from './volume-present-link.component';

describe('VolumePresentLinkComponent', () => {
  let component: VolumePresentLinkComponent;
  let fixture: ComponentFixture<VolumePresentLinkComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ VolumePresentLinkComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(VolumePresentLinkComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
