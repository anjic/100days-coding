import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IsePerformanceChartComponent } from './ise-performance-chart.component';

describe('IsePerformanceChartComponent', () => {
  let component: IsePerformanceChartComponent;
  let fixture: ComponentFixture<IsePerformanceChartComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IsePerformanceChartComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IsePerformanceChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
