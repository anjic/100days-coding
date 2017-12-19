import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IseDashboardComponent } from './ise-dashboard.component';

describe('IseDashboardComponent', () => {
  let component: IseDashboardComponent;
  let fixture: ComponentFixture<IseDashboardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IseDashboardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IseDashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
