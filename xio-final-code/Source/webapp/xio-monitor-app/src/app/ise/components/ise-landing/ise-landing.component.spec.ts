import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IseLandingComponent } from './ise-landing.component';

describe('IseLandingComponent', () => {
  let component: IseLandingComponent;
  let fixture: ComponentFixture<IseLandingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IseLandingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IseLandingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
