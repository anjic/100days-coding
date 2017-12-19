import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SangroupDashboardComponent } from './sangroup-dashboard.component';

describe('SangroupDashboardComponent', () => {
  let component: SangroupDashboardComponent;
  let fixture: ComponentFixture<SangroupDashboardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SangroupDashboardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SangroupDashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
