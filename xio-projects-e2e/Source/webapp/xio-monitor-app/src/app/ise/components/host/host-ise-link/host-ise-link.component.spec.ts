import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HostIseLinkComponent } from './host-ise-link.component';

describe('HostIseLinkComponent', () => {
  let component: HostIseLinkComponent;
  let fixture: ComponentFixture<HostIseLinkComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HostIseLinkComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HostIseLinkComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
