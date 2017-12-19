import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PerformanceVolumeComponent } from './ise-performance-volume.component';

describe('PerformanceVolumeComponent', () => {
  let component: PerformanceVolumeComponent;
  let fixture: ComponentFixture<PerformanceVolumeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PerformanceVolumeComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PerformanceVolumeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
