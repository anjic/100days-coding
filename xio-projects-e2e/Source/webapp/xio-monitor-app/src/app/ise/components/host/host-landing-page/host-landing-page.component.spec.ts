import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HostLandingPageComponent } from './host-landing-page.component';

describe('HostLandingPageComponent', () => {
  let component: HostLandingPageComponent;
  let fixture: ComponentFixture<HostLandingPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HostLandingPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HostLandingPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
