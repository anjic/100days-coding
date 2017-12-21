import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IsePerformanceComponent } from './ise-performance.component';

describe('IsePerformanceComponent', () => {
  let component: IsePerformanceComponent;
  let fixture: ComponentFixture<IsePerformanceComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IsePerformanceComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IsePerformanceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
