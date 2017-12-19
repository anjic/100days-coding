import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PerformanceHostComponent } from './ise-performance-host.component';

describe('PerformanceHostComponent', () => {
  let component: PerformanceHostComponent;
  let fixture: ComponentFixture<PerformanceHostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PerformanceHostComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PerformanceHostComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
