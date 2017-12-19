import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IseSangroupLinkComponent } from './ise-sangroup-link.component';

describe('IseSangroupLinkComponent', () => {
  let component: IseSangroupLinkComponent;
  let fixture: ComponentFixture<IseSangroupLinkComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IseSangroupLinkComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IseSangroupLinkComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
