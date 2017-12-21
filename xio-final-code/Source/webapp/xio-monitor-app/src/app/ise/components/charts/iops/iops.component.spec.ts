import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IopsComponent } from './iops.component';

describe('IopsComponent', () => {
  let component: IopsComponent;
  let fixture: ComponentFixture<IopsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IopsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IopsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
