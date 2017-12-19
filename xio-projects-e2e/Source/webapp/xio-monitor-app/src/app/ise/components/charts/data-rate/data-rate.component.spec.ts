import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DataRateComponent } from './data-rate.component';

describe('DataRateComponent', () => {
  let component: DataRateComponent;
  let fixture: ComponentFixture<DataRateComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DataRateComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DataRateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
